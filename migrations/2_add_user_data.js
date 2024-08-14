const { Sequelize, DataTypes } = require('sequelize');
const { db } = require('../config');

const sequelize = new Sequelize(db.url, {
  dialect: 'postgres',
  logging: false,
});

const User = sequelize.model('User');

module.exports = {
  up: async (queryInterface, Sequelize) => {
    await queryInterface.addColumn('Users', 'profilePicture', {
      type: Sequelize.STRING,
    });

    await queryInterface.addColumn('Users', 'bio', {
      type: Sequelize.STRING,
    });

    await queryInterface.addColumn('Users', 'website', {
      type: Sequelize.STRING,
    });

    await queryInterface.addColumn('Users', 'twitterHandle', {
      type: Sequelize.STRING,
    });

    await queryInterface.addColumn('Users', 'githubUsername', {
      type: Sequelize.STRING,
    });

    await queryInterface.addColumn('Users', 'linkedinProfile', {
      type: Sequelize.STRING,
    });
  },

  down: async (queryInterface, Sequelize) => {
    await queryInterface.removeColumn('Users', 'profilePicture');
    await queryInterface.removeColumn('Users', 'bio');
    await queryInterface.removeColumn('Users', 'website');
    await queryInterface.removeColumn('Users', 'twitterHandle');
    await queryInterface.removeColumn('Users', 'githubUsername');
    await queryInterface.removeColumn('Users', 'linkedinProfile');
  },
};
