const { Sequelize, DataTypes } = require('sequelize');
const { db } = require('../config');

const sequelize = new Sequelize(db.url, {
  dialect: 'postgres',
  logging: false,
});

const User = sequelize.define('User', {
  id: {
    type: DataTypes.INTEGER,
    primaryKey: true,
    autoIncrement: true,
  },
  username: {
    type: DataTypes.STRING,
    unique: true,
  },
  email: {
    type: DataTypes.STRING,
    unique: true,
  },
  password: {
    type: DataTypes.STRING,
  },
  location: {
    type: DataTypes.STRING,
  },
  deviceType: {
    type: DataTypes.STRING,
  },
  os: {
    type: DataTypes.STRING,
  },
  browser: {
    type: DataTypes.STRING,
  },
  language: {
    type: DataTypes.STRING,
  },
  timezone: {
    type: DataTypes.STRING,
  },
  createdAt: {
    type: DataTypes.DATE,
  },
  updatedAt: {
    type: DataTypes.DATE,
  },
});

const Transaction = sequelize.define('Transaction', {
  id: {
    type: DataTypes.INTEGER,
    primaryKey: true,
    autoIncrement: true,
  },
  userId: {
    type: DataTypes.INTEGER,
    references: {
      model: User,
      key: 'id',
    },
  },
  transactionType: {
    type: DataTypes.STRING,
  },
  amount: {
    type: DataTypes.DECIMAL(10, 2),
  },
  currency: {
    type: DataTypes.STRING,
  },
  timestamp: {
    type: DataTypes.DATE,
  },
  category: {
    type: DataTypes.STRING,
  },
  subcategory: {
    type: DataTypes.STRING,
  },
  description: {
    type: DataTypes.STRING,
  },
});

module.exports = {
  up: async (queryInterface, Sequelize) => {
    await queryInterface.createTable('Users', {
      id: {
        type: Sequelize.INTEGER,
        primaryKey: true,
        autoIncrement: true,
      },
      username: {
        type: Sequelize.STRING,
        unique: true,
      },
      email: {
        type: Sequelize.STRING,
        unique: true,
      },
      password: {
        type: Sequelize.STRING,
      },
      location: {
        type: Sequelize.STRING,
      },
      deviceType: {
        type: Sequelize.STRING,
      },
      os: {
        type: Sequelize.STRING,
      },
      browser: {
        type: Sequelize.STRING,
      },
      language: {
        type: Sequelize.STRING,
      },
      timezone: {
        type: Sequelize.STRING,
      },
      createdAt: {
        type: Sequelize.DATE,
      },
      updatedAt: {
        type: Sequelize.DATE,
      },
    });

    await queryInterface.createTable('Transactions', {
      id: {
        type: Sequelize.INTEGER,
        primaryKey: true,
        autoIncrement: true,
      },
      userId: {
        type: Sequelize.INTEGER,
        references: {
          model: 'Users',
          key: 'id',
        },
      },
      transactionType: {
        type: Sequelize.STRING,
      },
      amount: {
        type: Sequelize.DECIMAL(10, 2),
      },
      currency: {
        type: Sequelize.STRING,
      },
      timestamp: {
        type: Sequelize.DATE,
      },
      category: {
        type: Sequelize.STRING,
      },
      subcategory: {
        type: Sequelize.STRING,
      },
      description: {
        type: Sequelize.STRING,
      },
    });
  },

  down: async (queryInterface, Sequelize) => {
    await queryInterface.dropTable('Transactions');
    await queryInterface.dropTable('Users');
  },
};
